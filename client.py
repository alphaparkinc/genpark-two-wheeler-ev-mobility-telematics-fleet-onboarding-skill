class TwoWheelerEvMobilityTelematicsFleetOnboardingClient:
    def onboard_ev_driver_fleet(self, driver_national_id='NIN_99182310', battery_swap_station_id='BSS_LAGOS_VI_01'):
        return {
            'driver_id': 'max_drv_8841',
            'vehicle_type': 'MAX_M3_ELECTRIC_MOTORCYCLE',
            'battery_state_of_health_pct': 98.6,
            'iot_telematics_connected': True,
            'vehicle_financing_rent_to_own_daily_ngn': 3500.0,
            'nearest_battery_swap_station': battery_swap_station_id,
            'battery_swap_time_seconds': 45,
            'driver_safety_telematics_score': 94.2
        }
