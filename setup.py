import os
import sys

from distutils.core import setup


def run_bootstrap_and_configure():
    build_dir = 'giflossy_build'
    here = os.path.abspath(os.getcwd())

    os.chdir(here)
    print('- creating build dir...')
    os.system('mkdir -p %s' % build_dir)
    print('- bootstraping...')
    os.system('/bin/sh bootstrap.sh')
    print('- configure giflossy...')
    os.system('/bin/sh configure --disable-gifview \
                    --disable-gifdiff \
                    --prefix=%s/%s' % (here, build_dir))
    print('- make...')
    os.system('make')
    print('- make...')
    os.system('make install')
    cpy_cmd = 'cp {here}/{build_dir}/bin/gifsicle {here}/{build_dir}/bin/giflossy'.format(
        here=here,
        build_dir=build_dir
    )
    print('- name change: %s...' % cpy_cmd)
    os.system(cpy_cmd)


# 'install doesn't always call build for some reason
if 'install' in sys.argv and 'build' not in sys.argv:
    _index = sys.argv.index('install')
    sys.argv[:] = (
        sys.argv[:_index] + ['build', 'install'] + sys.argv[_index + 1:]
    )

    run_bootstrap_and_configure()


setup(
    name="pygiflossy",
    version="0.1.0",
    description="Gifsicle with superpowers like LZW compression",
    author="Krzysztof Klinikowski",
    author_email="kkszysiu@gmail.com",
    long_description=
    """Gifsicle with superpowers like LZW compression,
    crafted for Python
    """,
    scripts=['giflossy_build/bin/giflossy'],
    license="GPLv2",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion'
    ],
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['pygiflossy']
)
