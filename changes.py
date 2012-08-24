#
# Copyright (C) 2008 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import fcntl
import re
import os
import select
import sys
import subprocess
import pdb

from command import Command, MirrorSafeCommand
from git_command import GitCommand
from error import GitError


class Changes(Command, MirrorSafeCommand):
    common = False
    helpSummary = "List upstream changes on branches listed in manifest"
    helpUsage = """
    %prog [<project>...] [<arg>...]
    """
    helpDescription = """

    """

    def _Options(self, p):
        def cmd(option, opt_str, value, parser):
            setattr(parser.values, option.dest, list(parser.rargs))
            while parser.rargs:
            del parser.rargs[0]

        g = p.add_option_group('Output')
        g.add_option('-v', '--verbose',
                 dest='verbose', action='store_true',
                 help='Show status for all projects')

        def HasPendingChanges(self, project):
            if re.match("^[0-9a-f]{40}", project.revisionExpr):
                return False

            project.manifest._Load()

            if project.name == "manifests":
                project.revisionExpr = project.CurrentBranch
                localrev = project.bare_git.rev_parse(project.revisionExpr)
            else:
                localrev = project.GetRevisionId()

            cwd = project.worktree
            if self.manifest.IsMirror:
                cwd = project.gitdir
            if project.name == "manifests":
                remoteref = project.manifest.branch
            else:
                remoteref = project.revisionExpr
            if not re.match("^refs/heads/", remoteref):
                remoteref = "refs/heads/" + remoteref
            cmd = ["git ls-remote {0:s} | grep {1:s}".format(project.remote.name, remoteref)]
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
            stdout, stderr = p.communicate()
            r = p.wait()
            remoterev = stdout[0:40]
        return not remoterev == localrev

    def GetPendingChanges(self, project):
        if project.name == "manifests":
            branch = project.manifest.branch
        else:
            branch = project.revisionExpr

        cmdv = ["fetch", project.remote.name, branch]
        #print cmdv
        p = GitCommand(project,
                     cmdv,
                     capture_stdout=True,
                     capture_stderr=True)
        for line in p.process.stdout:
            if line[-1] == '\n':
                line = line[:-1]
            print line
        if p.Wait() != 0:
            raise GitError('%s GetPendingChanges: %s' % (
                           project.name,
                           p.stderr))

        format_str = "[%h]%x20%x20%ad%x20<%an>%x20%s"
        cmdv = ['log', '--date=short', '--pretty=format:%s' % format_str, 'HEAD..FETCH_HEAD']
        p = GitCommand(project,
                     cmdv,
                     capture_stdout=True,
                     capture_stderr=True)
        for line in p.process.stdout:
            if line[-1] == '\n':
                line = line[:-1]
            yield line
        if p.Wait() != 0:
            raise GitError('%s GetPendingChanges: %s' % (
                           project.name,
                           p.stderr))
        return

    def GetMaxProjectNameLength(self, opt, projects):
        if opt.verbose:
            return max([len(x.name) for x in projects])
        else:
            return max([len(x.name) if (not re.match("^[0-9a-f]{40}$", x.revisionExpr)) else 0 for x in projects])

    def Execute(self, opt, args):

        # Must check the manifest project itself along with all listed projects
        self.manifest._Load()
        projects = [self.manifest.manifestProject] + self.GetProjects(args)

        maxProjectNameLength = self.GetMaxProjectNameLength(opt, projects)

        numchanges = 0
        for project in projects:
            hasChanges = self.HasPendingChanges(project)

            if opt.verbose and re.match("^[0-9a-f]{40}$", project.revisionExpr):
                print "# {0:{1}s} no changes: Locked to [{2}]".format(project.name + '/',
                                                                      maxProjectNameLength + 3,
                                                                      project.GetRevisionId()[0:8])
            elif opt.verbose and not hasChanges:
                if (project.name != "manifests"):
                    remotebranch = project.revisionExpr
                    rev = project.GetRevisionId()
                else:
                    rev = project.bare_git.rev_parse(project.revisionExpr)
                    remotebranch = project.manifest.branch
                print "# {0:{1}s} no changes: HEAD matches {3}/{4} [{2}]".format(project.name + '/',
                                                                                 maxProjectNameLength + 3,
                                                                                 rev[0:8],
                                                                                 project.remote.name,
                                                                                 remotebranch)
            elif hasChanges:
                print "{0:s}".format(project.name + '/')
                for pc in self.GetPendingChanges(project):
                    numchanges += 1
                    print "{0:s}".format(pc)

        if numchanges == 0:
            sys.exit(1)
        else:
            sys.exit(0)
