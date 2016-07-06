#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sindre Sorhus
# Copyright (c) 2015 Sindre Sorhus
#
# License: MIT
#

from SublimeLinter.lint import RubyLinter


class ContentStyle(RubyLinter):
    cmd = "ruby /Users/jeremyhanson-finger/GitHub/content-lint/bin/content_lint_bin.rb"
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): '
        r'(:?(?P<warning>[RCW])|(?P<error>[EF])): '
        r'(?P<message>.+)')
    selectors = {
        'html': 'text.html.basic'
    }
    syntax = (
        'markdown',
        'markdown extended',
        'multimarkdown',
        'plain text',
        'ruby on rails',
        'ruby',
        'html'
    )
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>=0.0.0'
    tempfile_suffix = '-'
