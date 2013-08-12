#!/usr/bin/env python
# -*- coding: utf-8  -*-
################################################################################
#
#  sqlalchemy-pervasive -- SQLAlchemy Dialect for Pervasive PSQL
#  Copyright © 2013 Lance Edgar
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

"""
Support for the Pervasive PSQL database engine.
"""

from sqlalchemy.sql.compiler import SQLCompiler
from sqlalchemy.engine.default import DefaultDialect
from sqlalchemy.exc import InvalidRequestError


class PervasiveCompiler(SQLCompiler):
    """
    Custom SQL statement compiler for Pervasive PSQL.
    """

    # This logic was basically copied from the ``sqlalchemy-access`` dialect.

    def get_select_precolumns(self, select):
        s = 'DISTINCT ' if select._distinct else ''
        if select._limit:
            s += 'TOP {0} '.format(select._limit)
        if select._offset:
            raise InvalidRequestError(
                "Pervasive PSQL does not support TOP (limit) with an offset")
        return s

    def limit_clause(self, select):
        return ""


class PervasiveDialect(DefaultDialect):

    name = 'pervasive'

    statement_compiler = PervasiveCompiler