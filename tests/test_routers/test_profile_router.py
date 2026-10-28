import pytest

from app.models.notebooks import NotebookInformation
from app.models.parser import ParserFunction
from app.models.profiler import ProfilerFunction
from app.models.taxonomy import TaxonomyFunction
from app.routers.profile_router import _profile_notebook

example_of_notebook_info = NotebookInformation(name='test_file', parser_model=[], source_code="def f(x):" \
"   return x+2", parser_function=ParserFunction.VESPUCCI)

@pytest.mark.asyncio
async def test_profile_notebook():

    result = await _profile_notebook(example_of_notebook_info, taxonomy_name=TaxonomyFunction.DSPIPELINES, profiler_name=ProfilerFunction.DSPIPELINES)

    assert result['name'] == 'test_file'
    assert not result['outputs']
