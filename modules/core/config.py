import modules.core.save as save_module


CONFIG_DATA_FILE = 'resources/config.json'

def set_configs(configs):
    save_module.save_status(configs, CONFIG_DATA_FILE)

def get_configs() -> dict:
    return save_module.load_status(CONFIG_DATA_FILE)

def reset_configs():
    set_configs(
        {
            "volume": 50
        }
    )
