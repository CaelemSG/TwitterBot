import os

from qgis.core import (
    QgsGeometry,
    QgsMapSettings,
    QgsPrintLayout,
    QgsMapSettings,
    QgsMapRendererParallelJob,
    QgsLayoutItemLabel,
    QgsLayoutItemLegend,
    QgsLayoutItemMap,
    QgsLayoutItemPolygon,
    QgsLayoutItemScaleBar,
    QgsLayoutExporter,
    QgsLayoutItem,
    QgsLayoutPoint,
    QgsLayoutSize,
    QgsUnitTypes,
    QgsProject,
    QgsFillSymbol,
    QgsReadWriteContext,
)

from qgis.PyQt.QtGui import (
    QPolygonF,
    QColor,
)

from qgis.PyQt.QtCore import (
    QPointF,
    QRectF,
    QSize,
    QFile,
    QIODevice,
)

from qgis.PyQt.QtXml import (
    QDomDocument,
)

project = QgsProject.instance()
layout = QgsPrintLayout(project)

qfile = QFile("bot.qpt")
qfile.open(QIODevice.ReadOnly)

qdom = QDomDocument()
qdom.setContent(qfile)

qrw = QgsReadWriteContext()

ies = QgsLayoutExporter.ImageExportSettings()
ies.dpi = 25

layout.loadFromTemplate(qdom,qrw)
exporter = QgsLayoutExporter(layout)
exporter.exportToImage("./map.png",ies)