#!/usr/bin/env python
# -*- coding: utf-8 -*-

from application import create_app
app = create_app()
app.run(debug=True)
