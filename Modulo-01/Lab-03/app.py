hourRate = float(input("Horas Trabajadas: "))
payRate = float(input("Pago por hora: "))

overtimeHours = 0

if (hourRate > 40):
    overtimeHours = hourRate - 40