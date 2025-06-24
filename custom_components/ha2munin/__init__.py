from .http import setup_view

async def async_setup(hass, config):
    setup_view(hass)
    return True
