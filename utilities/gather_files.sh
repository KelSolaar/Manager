#/bin/bash
echo -------------------------------------------------------------------------------
echo Manager - Files Gathering
echo -------------------------------------------------------------------------------

export PROJECT_DIRECTORY=$(cd $( dirname "${BASH_SOURCE[0]}" )/..; pwd)

export DOCUMENTATION_DIRECTORY=$PROJECT_DIRECTORY/docs/
export RELEASES_DIRECTORY=$PROJECT_DIRECTORY/releases/
export REPOSITORY_DIRECTORY=$RELEASES_DIRECTORY/repository/
export UTILITIES_DIRECTORY=$PROJECT_DIRECTORY/utilities

#! Gathering folder cleanup.
rm -rf $REPOSITORY_DIRECTORY
mkdir -p $REPOSITORY_DIRECTORY/Manager

#! Manager Changes gathering.
cp -rf $RELEASES_DIRECTORY/Changes.html $REPOSITORY_DIRECTORY/Manager/

#! Manager Manual / Help files.
cp -rf $DOCUMENTATION_DIRECTORY/help $REPOSITORY_DIRECTORY/Manager/Help
rm $REPOSITORY_DIRECTORY/Manager/help/Manager_Manual.rst

#! Manager Api files.
cp -rf $DOCUMENTATION_DIRECTORY/sphinx/build/html $REPOSITORY_DIRECTORY/Manager/Api