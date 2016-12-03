# -*- coding: utf-8 -*-
#
# http://www.privacyidea.org
# (c) Cornelius Kölbel, privacyidea.org
#
# 2016-07-14 Martin Wheldon, <martin.wheldon@greenhills-it.co.uk>
#            Initial writeup
#
# This code is free software; you can redistribute it and/or
# modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
# License as published by the Free Software Foundation; either
# version 3 of the License, or any later version.
#
# This code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU AFFERO GENERAL PUBLIC LICENSE for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
The code of this module servers the AngularJS unittests 
"""
from flask import (Blueprint,
                   request,
                   send_from_directory)
import logging
from ..lib.log import log_with

log = logging.getLogger(__name__)

log.debug("made it here")

angulartesting_blueprint = Blueprint('angulartesting_blueprint', __name__, static_folder='static')

@angulartesting_blueprint.route('', methods=['GET'])
@angulartesting_blueprint.route('/', methods=['GET'])
@log_with(log)
def serve_e2e_test():
    """Serves the angular tests
    """
    log.debug("Helo")
    return send_from_directory('html', 'runner.html')
