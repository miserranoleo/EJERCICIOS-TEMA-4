def generar_calendario_basquet(num_equipos):
    calendario = []
    for dia in range(1, num_equipos):
        for equipo_local in range(num_equipos):
            equipo_visitante = (equipo_local + dia) % num_equipos
            calendario.append((equipo_local, equipo_visitante))
    return calendario

def generar_calendario_voley(num_equipos):
    calendario = []
    for dia in range(1, num_equipos):
        for equipo_local in range(num_equipos):
            equipo_visitante = (equipo_local + dia) % num_equipos
            if equipo_local != equipo_visitante:
                calendario.append((equipo_local, equipo_visitante))
    return calendario

def main():
    num_equipos_basquet = 10
    num_equipos_voley = 7

    calendario_basquet = generar_calendario_basquet(num_equipos_basquet)
    calendario_voley = generar_calendario_voley(num_equipos_voley)

    print("Calendario de torneos de básquet:")
    for i, partido in enumerate(calendario_basquet, start=1):
        print(f"Día {i}: Equipo {partido[0]} vs. Equipo {partido[1]}")

    print("\nCalendario de torneos de vóley:")
    for i, partido in enumerate(calendario_voley, start=1):
        print(f"Día {i}: Equipo {partido[0]} vs. Equipo {partido[1]}")

if __name__ == "__main__":
    main()
