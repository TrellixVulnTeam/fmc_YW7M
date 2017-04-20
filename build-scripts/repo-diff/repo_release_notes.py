# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import argparse
# import json
# import re

from ..modules.gitrepo.manifest_xml import XmlManifest
from ..modules.html.files import ReleaseNote

# from spyci import workspace
# from spyci.difflog import DiffLog
# from spyci.errors import Error
#from spyci.output import BuildSummary, ReleaseNote


def printLogs(project, otherProject, raw=False, color=True, pretty_format=None):

    logs = project.getAddedAndRemovedLogs(otherProject,
                                          oneline=(pretty_format is None),
                                          color=color,
                                          pretty_format=pretty_format)
    if logs['removed']:
        removedLogs = logs['removed'].split('\n')
        for log in removedLogs:
            if log.strip():
                if raw:
                    print('   R ' + log)

    if logs['added']:
        addedLogs = logs['added'].split('\n')
        for log in addedLogs:
            if log.strip():
                if raw:
                    print('   A ' + log)



def printRawDiff(diff):
    for project in diff['added']:
        print("A %s %s" % (project.relpath, project.revisionExpr))

    for project in diff['removed']:
        print("R %s %s" % (project.relpath, project.revisionExpr))

    for project, otherProject in diff['changed']:
        print("C %s %s %s" % (project.relpath, project.revisionExpr,
        otherProject.revisionExpr))
        printLogs(project, otherProject, raw=True, color=False)

    for project, otherProject in diff['unreachable']:
        print("U %s %s %s" % (project.relpath, project.revisionExpr,
        otherProject.revisionExpr))

def generate_release_note(  projectsFolder,
                            manifestPath1,
                            manifestPath2,
                            htmlTemplateFilePath):
    """
    Compares commits between two manifests revisions
    Generate a html report as an output

    """
    # Generate the diff thanks to git-repo module
    manifest1 = XmlManifest(projectsFolder)
    manifest1.Override(manifestPath1)

    manifest2 = XmlManifest(projectsFolder)
    manifest2.Override(manifestPath2)

    diff = manifest1.projectsDiff(manifest2)
    printRawDiff(diff)

    release_note_file = ReleaseNote("generated-RN.html")

    commitItems = []
    for project, otherProject in diff['changed']:
        commitItems.append("%s" % (project.relpath))
        logs = project.getAddedAndRemovedLogs(otherProject,
                                              oneline=True,
                                              color=False,
                                              pretty_format=None)
        if logs['removed']:
            removedLogs = logs['removed'].split('\n')
            for log in removedLogs:
                if log.strip():
                    commitItems.append(log)

        if logs['added']:
            addedLogs = logs['added'].split('\n')
            for log in addedLogs:
                if log.strip():
                    commitItems.append(log)

    release_note_file.render("release_note.html",
        product_name="Curie BSP",
        to_build="WW18",
        from_build="WW16",
        commit_items= commitItems
    )

if __name__ == "__main__":
    generate_release_note("/home/fabien/workspace/thunderdome/.repo/", "/home/fabien/workspace/thunderdome/manifest-ATP1XXXXXX-1651W0016.xml", "/home/fabien/workspace/thunderdome/manifest-ATP1XXXXXX-1652W0018.xml", "")
