# Sketches for fmu-dataio classes, or something else
Currently very immature, but if you want to test add this to
into rms script:

```
from fmu.tools.rms import import_localmodule


eh = import_localmodule(project, "export_helpers", path="../bin")


def export():
    inplace = eh.RmsInplaceVolumes(project, "Simgrid", "simgrid_volumes")
    # inplace = eh.RmsInplaceVolumes(project, "Geogrid", "geogrid_volumes")
    # print(inplace.report_output)
    inplace.export()

if __name__ == "__main__":
    export()


```