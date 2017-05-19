#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_api
----------------------------------
Tests for `api` module.
"""


class TestAPI:
    def test_api_get(self, client):
        res = client.get("/api/40000/48.888001,2.337442/restaurants")
        assert res.status_code == 200
