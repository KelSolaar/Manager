#/bin/bash
echo -------------------------------------------------------------------------------
echo Manager - Files Gathering
echo -------------------------------------------------------------------------------

export PROJECT=$( dirname "${BASH_SOURCE[0]}" )/..

export DOCUMENTATION=$PROJECT/docs/
export RELEASES=$PROJECT/releases/
export REPOSITORY=$RELEASES/repository/
export UTILITIES=$PROJECT/utilities

#! Gathering folder cleanup.
rm -rf $REPOSITORY
mkdir -p $REPOSITORY/Manager

#! Manager Changes gathering.
cp -rf $RELEASES/Changes.html $REPOSITORY/Manager/

#! Manager Manual / Help files.
cp -rf $DOCUMENTATION/help $REPOSITORY/Manager/Help
rm $REPOSITORY/Manager/help/Manager_Manual.rst

#! Manager Api files.
cp -rf $DOCUMENTATION/sphinx/build/html $REPOSITORY/Manager/Api