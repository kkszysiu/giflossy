import shutil
import subprocess
import tempfile
import os
import logging

logging.basicConfig()

logger = logging.getLogger(__name__)


def convert(input_filepath, output_filepath, optimize=True, compression_level=30, use_tmp=False, scale=(0, 0)):
    command = os.environ.get('GIFLOSSY_PATH') or 'giflossy'

    arguments = ['-w']

    if optimize:
        arguments.append('-O3')

    if compression_level:
        arguments.append('--lossy={0}'.format(compression_level))

    if all(scale):
        arguments.append('--resize-fit')
        arguments.append('x'.join([str(x) for x in scale]))

    arguments.append('-o')

    if use_tmp:
        tmp_output_dir = tempfile.mkdtemp(prefix='tmp-pygiflossy-')

        shutil.copy(input_filepath, tmp_output_dir)

        filename = os.path.basename(input_filepath)
        tmp_output_filepath = os.path.join(tmp_output_dir, filename)

        arguments.append(tmp_output_filepath)
    else:
        arguments.append(output_filepath)

    arguments.append(input_filepath)

    cmd = ' '.join([command] + arguments)

    try:
        logger.info('Running %s (%s)' % (command, cmd))
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError, inst:
        logger.exception('Running %s failed (exit status %s) (%s)' % (
            command, inst.returncode, cmd
        ))
    except OSError:
        logger.exception('Cannot run %s (%s)' % (command, cmd))

    if use_tmp:
        # cleanup
        try:
            shutil.copyfile(tmp_output_filepath, output_filepath)
            shutil.rmtree(tmp_output_dir, True)
        except OSError:
            pass


def crop(input_filepath, output_filepath, x, y, w, h, use_tmp=False):
    command = os.environ.get('GIFLOSSY_PATH') or 'giflossy'

    arguments = ['-w']

    arguments.append('--crop %i,%i+%ix%i' % (x, y, w, h))

    arguments.append('-o')

    if use_tmp:
        tmp_output_dir = tempfile.mkdtemp(prefix='tmp-pygiflossy-')

        shutil.copy(input_filepath, tmp_output_dir)

        filename = os.path.basename(input_filepath)
        tmp_output_filepath = os.path.join(tmp_output_dir, filename)

        arguments.append(tmp_output_filepath)
    else:
        arguments.append(output_filepath)

    arguments.append(input_filepath)

    cmd = ' '.join([command] + arguments)

    try:
        logger.info('Running %s (%s)' % (command, cmd))
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError, inst:
        logger.exception('Running %s failed (exit status %s) (%s)' % (
            command, inst.returncode, cmd
        ))
    except OSError:
        logger.exception('Cannot run %s (%s)' % (command, cmd))

    if use_tmp:
        # cleanup
        try:
            shutil.copyfile(tmp_output_filepath, output_filepath)
            shutil.rmtree(tmp_output_dir, True)
        except OSError:
            pass
