# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QuickDEMforJP
                                 A QGIS plugin
 The plugin to convert DEM to GeoTiff and Terrain RGB (Tiff).
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-05-31
        git sha              : $Format:%H$
        copyright            : (C) 2021 by MIERUNE Inc.
        email                : info@mierune.co.jp
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QuickDEMforJP class from file QuickDEMforJP.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .quick_dem_for_jp import QuickDEMforJP
    return QuickDEMforJP(iface)