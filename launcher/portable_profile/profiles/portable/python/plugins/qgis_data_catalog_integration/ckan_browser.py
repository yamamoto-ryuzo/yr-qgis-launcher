from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from qgis.core import QgsMessageLog, Qgis
from .ckan_browser_dialog import CKANBrowserDialog
from .ckan_browser_dialog_settings import CKANBrowserDialogSettings
import os.path
from .settings import Settings
from .util import Util

class CKANBrowser:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        QgsMessageLog.logMessage('__init__', 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Info)
        QSettings().setValue("ckan_browser/isopen", False)
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        QgsMessageLog.logMessage(u'plugin directory: {}'.format(self.plugin_dir), 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Info)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        QgsMessageLog.logMessage(u'locale: {}'.format(locale), 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Info)
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'CKANBrowser_{}.qm'.format(locale))

        locale_path_en = os.path.join(
            self.plugin_dir,
            'i18n',
            'CKANBrowser_en.qm'
        )

        # if we don't have translation for current locale, completely switch to English
        if not os.path.exists(locale_path):
            locale = 'en'
            locale_path = locale_path_en

        # if locale is not 'en' then additionally load 'en' as fallback for untranslated elements.
        if locale != 'en':
            QgsMessageLog.logMessage(u'loading "en" fallback: {}'.format(locale_path_en), 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Info)
            self.translator_en = QTranslator()
            self.translator_en.load(locale_path_en)
            if not QCoreApplication.installTranslator(self.translator_en):
                QgsMessageLog.logMessage(u'could not install translator: {}'.format(locale_path_en), 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Critical)
            else:
                QgsMessageLog.logMessage(u'locale "en" installed', 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Info)

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            if not QCoreApplication.installTranslator(self.translator):
                QgsMessageLog.logMessage(u'could not install translator: {}'.format(locale_path), 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Critical)
            else:
                QgsMessageLog.logMessage(u'locale "{}" installed'.format(locale), 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Info)

        self.settings = Settings()
        self.settings.load()
        self.util = Util(self.settings, self.iface.mainWindow())

        # TODO ping API

        # Create the dialog (after translation) and keep reference
#         self.dlg = CKANBrowserDialog(self.settings, self.iface, self.iface.mainWindow())

        # Declare instance attributes
        self.actions = []
        self.menu = self.util.tr(u'&Catalog Integration')
        # TODO: We are going to let the user set this up in a future iteration
        # installed translation file is searched first and the first translation file installed is searched last."
        if locale != 'en':
            QgsMessageLog.logMessage(u'loading "en" fallback: {}'.format(locale_path_en), 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Info)
            self.translator_en = QTranslator()
            self.translator_en.load(locale_path_en)
            if not QCoreApplication.installTranslator(self.translator_en):
                QgsMessageLog.logMessage(u'could not install translator: {}'.format(locale_path_en), 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Critical)
            else:
                QgsMessageLog.logMessage(u'locale "en" installed', 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Info)

        if os.path.exists(locale_path):
            self.translator = QTranslator()

            # load translations according to locale
            self.translator.load(locale_path)

            if not QCoreApplication.installTranslator(self.translator):
                QgsMessageLog.logMessage(u'could not install translator: {}'.format(locale_path), 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Critical)
            else:
                QgsMessageLog.logMessage(u'locale "{}" installed'.format(locale), 'QGIS Data Catalog Integration / Catalog Integration', Qgis.Info)

        self.settings = Settings()
        self.settings.load()
        self.util = Util(self.settings, self.iface.mainWindow())

        # TODO ping API

        # Create the dialog (after translation) and keep reference
#         self.dlg = CKANBrowserDialog(self.settings, self.iface, self.iface.mainWindow())

        # Declare instance attributes
        self.actions = []
        self.menu = self.util.tr(u'&Catalog Integration')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'Catalog Integration')
        self.toolbar.setObjectName(u'Catalog Integration')


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the InaSAFE toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')

        self.add_action(
            icon_path,
            text=self.util.tr(u'Catalog Integration'),
            callback=self.run,
            parent=self.iface.mainWindow()
        )
        
        icon_settings = os.path.join(os.path.dirname(__file__), 'icon-settings.png')
        
        self.add_action(
            icon_settings,
            text=self.util.tr(u'ckan_browser_settings'),
            callback=self.open_settings,
            parent=self.iface.mainWindow()
        )

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.util.tr(u'&Catalog Integration'),
                action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        """Run method that performs all the real work"""
        
        is_open = QSettings().value("ckan_browser/isopen", False)
        #Python treats almost everything as True````
        #is_open = bool(is_open)
        self.util.msg_log_debug(u'isopen: {0}'.format(is_open))
        
        #!!!string comparison - Windows and Linux treat it as string, Mac as bool
        # so we convert string to bool
        if isinstance(is_open, str):
            is_open = self.util.str2bool(is_open)
        
        if is_open:
            self.util.msg_log_debug(u'Dialog already opened')
            return
        
        # auf URL testen
        dir_check = self.util.check_dir(self.settings.cache_dir)
        api_url_check = self.util.check_api_url(self.settings.ckan_url)
        if dir_check is False or api_url_check is False:
            dlg = CKANBrowserDialogSettings(self.settings, self.iface, self.iface.mainWindow())
            dlg.show()
            result = dlg.exec_()
            if result != 1:
                return

#         self.util.msg_log('cache_dir: {0}'.format(self.settings.cache_dir))

        try:
            QSettings().setValue("ckan_browser/isopen", True)
            self.dlg = CKANBrowserDialog(self.settings, self.iface, self.iface.mainWindow())

            # show the dialog
            self.dlg.show()
            #self.dlg.open()
            # Run the dialog event loop
            result = self.dlg.exec_()
            # See if OK was pressed
            if result:
                pass
        finally:
            QSettings().setValue("ckan_browser/isopen", False)

    def open_settings(self):
        dlg = CKANBrowserDialogSettings(self.settings, self.iface, self.iface.mainWindow())
        dlg.show()
        dlg.exec_()