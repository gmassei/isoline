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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from isolinedialog import isolineDialog
import os.path
import subprocess


class isoline:

	def __init__(self, iface):
		# Save reference to the QGIS interface
		self.iface = iface
		# initialize plugin directory
		self.plugin_dir = os.path.dirname(__file__)
		# initialize locale
		locale = QSettings().value("locale/userLocale")[0:2]
		localePath = os.path.join(self.plugin_dir, 'i18n', 'isoline_{}.qm'.format(locale))
		if os.path.exists(localePath):
			self.translator = QTranslator()
			self.translator.load(localePath)
			if qVersion() > '4.3.3':
				QCoreApplication.installTranslator(self.translator)
		self.canvas = self.iface.mapCanvas()
		# Our tool will emit a QgsPoint for each click
		self.clickTool = QgsMapToolEmitPoint(self.canvas)
		#inizialize activeLayer
		self.aLayer=self.iface.activeLayer()

		
	def initGui(self):
		# Create action that will start plugin configuration
		self.action = QAction(
			QIcon(":/plugins/isoline/icon.png"),
			u"isoline", self.iface.mainWindow())
		# connect the action to the run method
		self.action.triggered.connect(self.run)
		#QObject.connect(self.action, SIGNAL("triggered()"), self.run)
		result = QObject.connect(self.clickTool, SIGNAL(
			"canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.getPoint)
		# Add toolbar button and menu item
		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu(u"&isoline", self.action)

	def unload(self):
		# Remove the plugin menu item and icon
		self.iface.removePluginMenu(u"&isoline", self.action)
		self.iface.removeToolBarIcon(self.action)
		
	def getPoint(self, point, button):
		self.aLayer=self.iface.activeLayer()
		pt = QgsPoint(point.x(),point.y())
		value=self.aLayer.dataProvider().identify(pt, QgsRaster.IdentifyFormatValue).results()
		QgsMessageLog.logMessage("%s" % str(pt),"Info", QgsMessageLog.INFO)
		self.makeIsoline(value)
			
	def outFile(self):
		outvLayer = QFileDialog.getSaveFileName(None, "Output map",".", "ESRI Shapefile (*.shp)")
		return outvLayer
	
	def makeIsoline(self,value):
		source=self.aLayer.source()
		outPath=self.outFile()
		stringa=str('gdal_contour -a elev -fl ' + str(value[1]) +' '+ source  + ' ' + outPath)
		QgsMessageLog.logMessage("%s" % (stringa),"comando", QgsMessageLog.INFO)
		check=subprocess.call(stringa)
		if check==0:
			iso=QgsVectorLayer(outPath, 'isoline [%s]' % str(value[1]), 'ogr')
			QgsMapLayerRegistry.instance().addMapLayer(iso)
		else:
			QMessageBox.critical(None, 'Error ! ' , 'Error in generating file (overwrite isn\'t allowed)')
		return 0

	# run method that performs all the real work
	def run(self):
		self.canvas.setMapTool(self.clickTool)
