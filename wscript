srcdir = '.'
blddir = 'build'
VERSION = '0.0.1'

nonmac = False

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')
  if not conf.check(lib=['sfml-system','sfml-window','sfml-graphics','sfml-audio'], uselib_store='SFML'):
    conf.fatal("Cannot find SFML")
  if not conf.check(lib='openal', uselib_store='AL'):
    conf.fatal("Cannot find openal")
  if not conf.check(lib='sndfile', uselib_store='SNDFILE'):
    conf.fatal("Cannot find sndfile")


def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon', framework=['OpenAL','SFML','sfml-system','sfml-window','sfml-graphics','sfml-audio'])
  obj.uselib=['SFML','AL','SNDFILE']
  obj.target = 'nodesfml'
  obj.source = 'src/NodeSFML.cc'
