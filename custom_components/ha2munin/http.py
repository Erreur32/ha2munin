from homeassistant.components.http import HomeAssistantView

DOMAIN = "ha2munin"

async def async_setup(hass, config):
    hass.http.register_view(MuninAPI())
    return True

class MuninAPI(HomeAssistantView):
    url = "/api/munin"
    name = "api:munin"

    async def get(self, request):
        # Exemple : récupère quelques sensors connus
        entity_ids = [
            "sensor.system_monitor_processor_use",
            "sensor.system_monitor_memory_usage",
            "sensor.system_monitor_processor_temperature",
            "sensor.system_monitor_swap_use",
            "sensor.system_monitor_load_1m",
            "sensor.system_monitor_load_5m",
            "sensor.system_monitor_load_15m",
            "sensor.system_monitor_disk_usage",
            "sensor.system_monitor_disk_use",
            "sensor.system_monitor_disk_use_media",
            "sensor.system_monitor_memory_use",
            "sensor.system_monitor_network_throughput_in_enp3s0",
            "sensor.system_monitor_network_throughput_out_enp3s0"
        ]
        data = {}
        for eid in entity_ids:
            state = request.app["hass"].states.get(eid)
            data[eid] = state.state if state else "U"
        # Retourne sous forme texte (façon plugin Munin)
        lines = [f"{eid.replace('sensor.system_monitor_', '')}.value {val}" for eid, val in data.items()]
        return self.json({"output": "\n".join(lines)})
