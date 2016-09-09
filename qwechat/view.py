from PyQt5.QtCore import QUrl, QUrlQuery
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWebEngineWidgets import (QWebEngineSettings, QWebEngineView,
                                      QWebEnginePage)


class View(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        page = Page(self)
        page.settings().setAttribute(
            QWebEngineSettings.JavascriptCanAccessClipboard, True)
        self.setPage(page)


class Page(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__()
        profile = self.profile()
        profile.setHttpUserAgent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit"
                                 "/537.36 (KHTML, like Gecko) Chrome"
                                 "/54.0.2810.2 Safari/537.36")

    def acceptNavigationRequest(self, url, _type, isMainFrame):
        print(url)
        if url.url().endswith('fake'):
            return False
        query = QUrlQuery(url)
        if query.hasQueryItem("requrl"):
            orig_url = query.queryItemValue("requrl", QUrl.FullyDecoded)
            url = QUrl(orig_url)
            QDesktopServices.openUrl(url)
            return False
        return super().acceptNavigationRequest(url, _type, isMainFrame)
