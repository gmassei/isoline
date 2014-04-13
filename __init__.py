# -*- coding: utf-8 -*-
"""
/***************************************************************************
 isoline
                                 A QGIS plugin
 make a single isoline to a specific value
                             -------------------
        begin                : 2014-03-24
        copyright            : (C) 2014 by Gianluca Massei
        email                : g_massa@libero.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load isoline class from file isoline
    from isoline import isoline
    return isoline(iface)
