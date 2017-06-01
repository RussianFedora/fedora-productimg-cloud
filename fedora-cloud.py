from pyanaconda.installclasses.fedora import FedoraBaseInstallClass
from pyanaconda.constants import *
from pyanaconda.product import *
from pyanaconda import network
from pyanaconda import nm
from pyanaconda import iutil
import types
from pyanaconda.kickstart import getAvailableDiskSpace
from blivet.partspec import PartSpec
from blivet.autopart import swap_suggestion
from blivet.platform import platform
from blivet.size import Size

class FedoraCloudInstallClass(FedoraBaseInstallClass):
    name = "Fedora Cloud"
    stylesheet = "/usr/share/anaconda/fedora-cloud.css"
    sortPriority = FedoraBaseInstallClass.sortPriority + 1
    defaultPackageEnvironment = "rfremix-cloud-server-environment"

    def setDefaultPartitioning(self, storage):
        autorequests = [PartSpec(mountpoint="/", fstype=storage.default_fstype,
                                 size=Size("2GiB"),
                                 grow=True,
                                 btr=False, lv=False, thin=True, encrypted=False)]

        bootreqs = platform.set_default_partitioning()
        if bootreqs:
            autorequests.extend(bootreqs)

        for autoreq in autorequests:
            if autoreq.fstype is None:
                if autoreq.mountpoint == "/boot":
                    autoreq.fstype = storage.default_boot_fstype
                    autoreq.size = Size("300MiB")
                else:
                    autoreq.fstype = storage.default_fstype

        storage.autopart_requests = autorequests
