# coding=utf-8

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame.py3compat import *
from libqtopensesame.misc.config import cfg
from pyqode.language_server.backend.workers import (
    SERVER_ERROR,
    SERVER_RUNNING,
    SERVER_NOT_STARTED
)
from pyqode.core.widgets import SplittableCodeEditTabWidget
from libqtopensesame.extensions import BaseExtension
from libqtopensesame.misc.translate import translation_context
_ = translation_context('LanguageServer', category=u'extension')


class LanguageServer(BaseExtension):
    
    preferences_ui = 'extensions.LanguageServer.preferences'

    def event_startup(self):

        if cfg.lsp_enable_r:
            from lsp_code_edit_widgets import RCodeEdit
            RCodeEdit.extension_manager = self.extension_manager
            SplittableCodeEditTabWidget.register_code_edit(RCodeEdit)
        if cfg.lsp_enable_css:
            from lsp_code_edit_widgets import CSSCodeEdit
            CSSCodeEdit.extension_manager = self.extension_manager
            SplittableCodeEditTabWidget.register_code_edit(CSSCodeEdit)
        if cfg.lsp_enable_python:
            from lsp_code_edit_widgets import PythonCodeEdit
            PythonCodeEdit.extension_manager = self.extension_manager
            SplittableCodeEditTabWidget.register_code_edit(PythonCodeEdit)
        if cfg.lsp_enable_typescript:
            from lsp_code_edit_widgets import TypeScriptCodeEdit
            TypeScriptCodeEdit.extension_manager = self.extension_manager
            SplittableCodeEditTabWidget.register_code_edit(TypeScriptCodeEdit)

    def _on_server_status_changed(self, langid, cmd, status, pid):
        
        if (
            status == SERVER_RUNNING and
            pid not in self.extension_manager.provide('subprocess_pids')
        ):
            self.extension_manager.fire(
                'notify',
                message='{} language server started'.format(langid),
                category='info'
            )
            self.extension_manager.fire(
                'register_subprocess',
                pid=pid,
                description=cmd
            )
        elif status == SERVER_NOT_STARTED:
            self.extension_manager.fire(
                'notify',
                message='{} language server stopped'.format(langid),
                category='warning'
            )
        elif status == SERVER_ERROR:
            self.extension_manager.fire(
                'notify',
                message=(
                    'Failed to start {} language server ({}). Visit '
                    'https://rapunzel.cogsci.nl/language-server for '
                    'instructions.'
                ).format(
                    langid,
                    cmd
                ),
                category='warning'
            )

    def event_register_editor(self, editor, mime_type=u'text/plain'):

        if hasattr(editor, 'server_status_changed'):
            editor.server_status_changed.connect(
                self._on_server_status_changed
            )

    def event_ide_project_folders_changed(self, folders):
        
        pids = []
        for editor in self.extension_manager.provide('ide_editors'):
            if not hasattr(editor, 'change_project_folders'):
                continue
            pid = editor.language_server_pid
            if pid in pids:
                continue
            editor.change_project_folders(folders)
            pids.append(pid)
