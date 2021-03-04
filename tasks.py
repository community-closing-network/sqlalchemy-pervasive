# -*- coding: utf-8; -*-
################################################################################
#
#  sqlalchemy-pervasive -- SQLAlchemy Dialect for Pervasive PSQL
#  Copyright © 2013-2021 Sacramento Natural Foods Co-op, Inc
#
#  This file is part of sqlalchemy-pervasive.
#
#  sqlalchemy-pervasive is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by the
#  Free Software Foundation, either version 3 of the License, or (at your
#  option) any later version.
#
#  sqlalchemy-pervasive is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#  or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  sqlalchemy-pervasive.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import os
import shutil

from invoke import task


here = os.path.abspath(os.path.dirname(__file__))
exec(open(os.path.join(here, 'sqlalchemy_pervasive', '_version.py')).read())


@task
def release(ctx):
    """
    Release a new version of 'sqlalchemy-pervasive'.
    """
    shutil.rmtree('sqlalchemy_pervasive.egg-info')
    ctx.run('python setup.py sdist --formats=gztar')
    ctx.run('twine upload dist/sqlalchemy-pervasive-{}.tar.gz'.format(__version__))
