#! /usr/bin/env python3

import tempfile
import shutil
from pathlib import Path
import datetime
import pytz

from scene_select.check_ancillary import AncillaryFiles

BRDF_TEST_DIR = Path(__file__).parent.joinpath("test_data", "BRDF")
WV_TEST_DIR = Path(__file__).parent.joinpath("test_data", "water_vapour")


def test_ancillaryfiles_local():
    # no water v data for these years
    af_ob = AncillaryFiles(brdf_dir=BRDF_TEST_DIR, water_vapour_dir=WV_TEST_DIR)
    a_dt = datetime.datetime(1944, 6, 4, tzinfo=pytz.UTC)
    assert not af_ob.definitive_ancillary_files(a_dt)
    a_dt = datetime.datetime(2018, 6, 4, tzinfo=pytz.UTC)
    assert not af_ob.definitive_ancillary_files(a_dt)

    # no water v data - explore more
    a_dt = datetime.datetime(2020, 8, 13, tzinfo=pytz.UTC)
    assert not af_ob.definitive_ancillary_files(a_dt)

    #  water v data - no BRDF
    a_dt = datetime.datetime(2020, 8, 2, tzinfo=pytz.UTC)
    assert not af_ob.definitive_ancillary_files(a_dt)

    #  water v data - no BRDF - but that is ok, before BDF started
    a_dt = datetime.datetime(2002, 2, 2, tzinfo=pytz.UTC)
    assert af_ob.definitive_ancillary_files(a_dt)

    #  water v data  BRDF
    a_dt = datetime.datetime(2020, 8, 1, tzinfo=pytz.UTC)
    assert af_ob.definitive_ancillary_files(a_dt)

    #  water v data  BRDF - different time zone format
    a_dt = datetime.datetime(2020, 8, 1, tzinfo=datetime.timezone.utc)
    assert af_ob.definitive_ancillary_files(a_dt)


def test_ancillaryfiles_water():

    # BRDF there. last day out of wv data
    af_ob = AncillaryFiles(brdf_dir=BRDF_TEST_DIR, water_vapour_dir=WV_TEST_DIR)
    a_dt = datetime.datetime(2020, 8, 9, tzinfo=pytz.UTC)
    assert af_ob.definitive_ancillary_files(a_dt)

    #  BRDF there. one day out from wv data
    a_dt = datetime.datetime(2020, 8, 10, tzinfo=pytz.UTC)
    assert af_ob.definitive_ancillary_files(a_dt)

    #  BRDF there. two days out from wv data
    a_dt = datetime.datetime(2020, 8, 11, tzinfo=pytz.UTC)
    assert not af_ob.definitive_ancillary_files(a_dt)
