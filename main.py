import datetime
import time
import os

def main():
  action = 1

  while True:
    clearTerminal()
    if action == 1:
      action = menu()
    elif action == 2:
      action = registerPatient()
    elif action == 3:
      action = scheduleAppointment()
    elif action == 4:
      action = deleteAppointment()
    elif action == 0:
      close()


def clearTerminal():
  os.system('clear')


def menu():
  print("---------------------------------------------")
  print("  Bem-vindo(a) a Cliníca de Consultas Ágil!  ")
  print("---------------------------------------------\n")

  option = -1
  while True:
    print("Essas são as ações possíveis:\n")
    print("1 - Cadastrar um paciente")
    print("2 - Marcar uma consulta")
    print("3 - Cancelar uma consultas")
    print("0 - Sair\n")

    try:
      option = int(input("Digite o número da ação desejada: "))
      if option >= 0 and option <= 3:
        break
      else:
        print("Opção inválida! Tente novamente.")
        time.sleep(2)
        clearTerminal()

    except ValueError:
      print("\nDigite apenas números!\n")
      time.sleep(2)
      clearTerminal()

  if option == 0:
    return 0
  else:
    return option + 1


def readPatients():
  patients = {}
  try:
    with open("patients.txt", "r") as file:
      for line in file:
        name, phone = line.strip().split(",")
        patients[phone] = name
  except FileNotFoundError:
    with open("patients.txt", "w") as file:
      pass
  return patients


def writePatients(patients):
  with open("patients.txt", "w") as file:
    for phone in patients:
      file.write(f"{patients[phone]},{phone}\n")


def registerPatient():
  patients = readPatients()
  
  while True:
    clearTerminal()
    print("\nPara cadastrar um paciente, insira o nome do paciênte:\n")
    name = input("Nome: ")
    if name == "":
      print("Nome inválido! Tente novamente.")
      time.sleep(2)
      continue
    else:
      break

  while True:
    clearTerminal()
    print("\nPara concluir o cadastro, insira o telefone do paciente:")
    print("Formato: (XX) XXXXX-XXXX\n")
    phone = input("Telefone: ")
    if phone == "":
      print("Telefone inválido! Tente novamente.")
      time.sleep(2)
      continue
    else:
      if patients.get(phone) is not None:
        print("\nPaciente já cadastrado!")
        time.sleep(2)
        continue
      break

  patients[phone] = name
  writePatients(patients)

  clearTerminal()
  print("\nPaciente cadastrado com sucesso!\n")
  time.sleep(2)
  return 1


def readAppointments():
  appointments = {}
  try:
    with open("appointments.txt", "r") as file:
      for line in file:
        date, hour, speciality, phone, name = line.strip().split(",")
        day = appointments.get(date) or {}
        day[hour] = {
          "speciality": speciality,
          "phone": phone,
          "name": name
        }
        appointments[date] = day
  except FileNotFoundError:
    with open("appointments.txt", "w") as file:
      pass
  return appointments

def writeAppointments(appointments):
  with open("appointments.txt", "w") as file:
    for date in appointments:
      day = appointments[date]
      for hour in day:
        appointment = day[hour]
        file.write(f"{date},{hour},{appointment['speciality']},{appointment['phone']},{appointment['name']}\n")


def scheduleAppointment():
  appointments = readAppointments()
  patients = readPatients()
  while True:
    clearTerminal()
    print("\nPara marcar uma consulta, selecione um paciente:")
    print("Número - Telefone - Nome\n")
    index = 1
    for phone in patients:
      print(f"{index}. {phone} - {patients[phone]}")
      index = index + 1

    try:
      option = int(input("\nDigite o número do paciente: "))
      if option >= 1 and option <= len(patients):
        break
      else:
        print("Opção inválida! Tente novamente.")
        time.sleep(2)
    except ValueError:
      print("\nDigite apenas números!\n")
      time.sleep(2)

  phone = list(patients.keys())[option - 1]
  appointmentDate = ""
  while True:
    clearTerminal()
    print(f"Paciente selecionado(a): {patients[phone]}")
    print("\nPara prosseguir, digite a data no formato DD/MM/AAAA:\n")
    inputDate = input("Data: ")
    if inputDate == "":
      print("Data inválida! Tente novamente.")
      time.sleep(2)
      continue
    else:
      try:
        date = datetime.datetime.strptime(inputDate, "%d/%m/%Y")
        if date < datetime.datetime.now():
          print("Data inválida! Tente novamente.")
          time.sleep(2)
          continue
        appointmentDate = inputDate
        break
      except ValueError:
        print("Data inválida! Tente novamente.")
        time.sleep(2)

  appointmentHour = ""
  while True:
    clearTerminal()
    print(f"Paciente selecionado(a): {patients[phone]}")
    print(f"Data selecionada: {appointmentDate}")
    print("\nPara prosseguir, digite a hora no formato HH:MM:\n")
    inputHour = input("Hora: ")
    if inputHour == "":
      print("Hora inválida! Tente novamente.")
      time.sleep(2)
      continue
    else:
      try:
        hour = datetime.datetime.strptime(inputHour, "%H:%M").time
        appointmentHour = inputHour
        day = appointments.get(appointmentDate) or {}
        if day.get(inputHour) is not None:
          print("Horário indisponível! Tente novamente.")
          time.sleep(2)
          continue
        break
      except ValueError:
        print("Hora inválida! Tente novamente.")
        time.sleep(2)

  appointmentSpeciality = ""
  while True:
    clearTerminal()
    print(f"Paciente selecionado(a): {patients[phone]}")
    print(f"Data selecionada: {appointmentDate}")
    print(f"Hora selecionada: {appointmentHour}")
    print("\nPara prosseguir, digite a especialidade do médico:\n")
    inputSpeciality = input("Especialidade: ")
    if inputSpeciality == "":
      print("Especialidade inválida! Tente novamente.")
      time.sleep(2)
      continue
    else:
      appointmentSpeciality = inputSpeciality
      break

  day = appointments.get(appointmentDate) or {}
  day[appointmentHour] = {
    "speciality": appointmentSpeciality,
    "phone": phone,
    "name": patients[phone]
  }
  appointments[appointmentDate] = day
  writeAppointments(appointments)

  clearTerminal()
  print("\nConsulta marcada com sucesso!\n")
  time.sleep(2)
  return 1


def deleteAppointment():
  appointments = readAppointments()
  while True:
    clearTerminal()
    print("\nSelecione a consulta que deseja excluir:")
    print("Número - Data - Hora - Especialidade - Telefone - Nome\n")
    index = 1
    for date in appointments:
      day = appointments[date]
      for hour in day:
        appointment = day[hour]
        print(f"{index}. {date} - {hour} - {appointment['speciality']} - {appointment['phone']} - {appointment['name']}")
        index = index + 1

    try:
      option = int(input("\nDigite o número da consulta: "))
      if option >= 1 and option <= index:
        break
      else:
        print("Opção inválida! Tente novamente.")
        time.sleep(2)
    except ValueError:
      print("\nDigite apenas números!\n")
      time.sleep(2)

  date = ""
  hour = ""
  appointment = {}
  index = 1
  for date in appointments:
    day = appointments[date]
    for hour in day:
      appointment = day[hour]
      if index == option:
        date = date
        hour = hour
        appointment = appointment
        break
  
  while True:
    clearTerminal()
    print("Consulta selecionada:\n")
    print(f"Data: {date}")
    print(f"Hora: {hour}")
    print(f"Especialidade: {appointment['speciality']}")
    print(f"Telefone do(a) paciente: {appointment['phone']}")
    print(f"Nome do(a) paciente: {appointment['name']}\n")
    print("Deseja realmente excluir a consulta? (S/N)")

    option = input("Opção: ")
    if option == "S" or option == "s" or option == "Sim" or option == "sim":
      day = appointments.get(date) or {}
      day.pop(hour)
      appointments[date] = day
      writeAppointments(appointments)
      clearTerminal()
      print("\nConsulta excluída com sucesso!\n")
      time.sleep(2)
      break
    elif option == "N" or option == "n" or option == "Não" or option == "não":
      clearTerminal()
      print("\nExclusão cancelada!\n")
      time.sleep(2)
      break
    else:
      print("Opção inválida! Tente novamente.")
      time.sleep(2)

  return 1

def close():
  print("\nObrigado por usar o sistema!\n")
  time.sleep(2)
  exit()


main()