import os
from lessons.lesson import Lesson, Step
from lessons.utils import *
from qgis.utils import iface
from lessons import addLessonModule
from lessons.utils import copyLessonData


def copyTable():
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Transform_X_and_Y_CSV_table_into_a_point_vector_layer/data", "songs.csv")
    copyLessonData(filepath, os.path.basename(os.path.dirname(__file__)))


lesson = Lesson ("07. Transform X and Y CSV table into a point vector layer",
                 "General tasks", "lesson.html")

lesson.addStep("Copy data", "Copy data", copyTable)
lesson.addStep('Introduction', 'introduction.html', steptype=Step.MANUALSTEP)
lesson.addMenuClickStep('Layer/Add Layer/Add Delimited Text Layer...')
lesson.addStep('Configure importing settings', 'delimited_text_settings.html', steptype=Step.MANUALSTEP)
lesson.addStep('Set layer as active layer', 'set_active_layer.html', steptype=Step.MANUALSTEP)
lesson.addMenuClickStep('Layer/Save As...')
lesson.addStep('Save the file as GeoPackage', 'save_as_geopackage.html', steptype=Step.MANUALSTEP)

lesson.addNextLesson("General tasks", "08. Group layers")