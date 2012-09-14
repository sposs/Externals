#!/usr/bin/env python

import imp, os, sys, platform, shutil

here = os.path.dirname( os.path.abspath( __file__ ) )
chFilePath = os.path.join( os.path.dirname( here ) , "common", "CompileHelper.py" )
try:
  fd = open( chFilePath )
except Exception, e:
  print "Cannot open %s: %s" % ( chFilePath, e )
  sys.exit( 1 )

chModule = imp.load_module( "CompileHelper", fd, chFilePath, ( ".py", "r", imp.PY_SOURCE ) )
fd.close()
chClass = getattr( chModule, "CompileHelper" )

ch = chClass( here )

versions = { 'Imaging' : "1.1.6",
             'matplotlib' : '0.99.1.1',
             'numpy' : '1.3.0' }

ch.setPackageVersions( versions )
env = { 'PKG_CONFIG_PATH' : os.path.join( ch.getPrefix(), "lib", "pkgconfig" ) }
ch.setDefaultEnv( env )
for package in ( 'numpy', 'Imaging', 'matplotlib' ):
  if not ch.downloadPackage( package ):
    ch.ERROR( "Could not download %s" % package )
  if not ch.unTarPackage( package ):
    ch.ERROR( "Could not deploy %s" % package )
    sys.exit( 1 )
  fd = open( os.path.join( ch.getPackageDir( package ), "site.cfg" ), "w" )
  fd.write( """\
[DEFAULT]
library_dirs=%s
include_dirs=%s
""" % ( ", ".join( ch.getPrefixLibDirs() ), ", ".join( ch.getPrefixIncludeDirs() ) ) )
  fd.close()

  packageDir = ch.getPackageDir( package )
  if package == "matplotlib":
    shutil.copy( os.path.join( here, "setupext.py" ),
                 os.path.join( packageDir, "setupext.py" ) )

  if not ch.easyInstall( packageDir ):
    ch.ERROR( "Could not deploy %s" % package )
    sys.exit( 1 )