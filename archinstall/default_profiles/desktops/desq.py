from typing import List, Optional, Any, TYPE_CHECKING

from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

if TYPE_CHECKING:
	_: Any

class DesqProfile(XorgProfile):
	def __init__(self):
		super().__init__('DesQ', ProfileType.DesktopEnv, description='')

	@property
	def packages(self) -> List[str]:
		return [
			"desq-shell",
			"desq-apps-term",
			"desq-utils-keyring",
			"desq-utils-lock",
			"desq-utils-notifier",
			"desq-utils-powermanager",
			"desq-apps-archiver"
		]

	@property
	def default_greeter_type(self) -> Optional[GreeterType]:
		return GreeterType.Sddm
