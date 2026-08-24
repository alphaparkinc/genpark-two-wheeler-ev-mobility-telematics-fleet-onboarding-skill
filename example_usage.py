from client import TwoWheelerEvMobilityTelematicsFleetOnboardingClient

def main():
    client = TwoWheelerEvMobilityTelematicsFleetOnboardingClient()
    res = client.onboard_ev_driver_fleet('NIN_88192033', 'BSS_LEKKI_02')
    print('Driver: ' + res['driver_id'] + ' | Vehicle: ' + res['vehicle_type'])
    print('Battery SOH: ' + str(res['battery_state_of_health_pct']) + '% | Swap Time: ' + str(res['battery_swap_time_seconds']) + 's')
    print('Rent-to-Own: NGN ' + str(res['vehicle_financing_rent_to_own_daily_ngn']) + '/day (Safety: ' + str(res['driver_safety_telematics_score']) + '/100)')

if __name__ == '__main__':
    main()
