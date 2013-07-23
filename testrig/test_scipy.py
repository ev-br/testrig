GIT_SOURCES = [
    ('numpy', 'git://github.com/numpy/numpy.git', 'master'),
    ('scipy', 'git://github.com/scipy/scipy.git', 'master')
]

def run(fixture):
    fixture.pip_install("nose")
    fixture.git_install(GIT_SOURCES)
    fixture.run_numpytest("scipy")
