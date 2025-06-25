from datetime import date, datetime, timezone

users = [
    {
        "name": "João Batista",
        "username": "joaob",
        "password": "senha123"
    },
    {
        "name": "Mariana Silva",
        "username": "marisilva",
        "password": "teste456"
    },
    {
        "name": "Carlos Mendes",
        "username": "cmendes",
        "password": "1234abcd"
    },
    {
        "name": "Ana Clara Souza",
        "username": "anaclara",
        "password": "minhasenha"
    },
]


trucks = [
    {
        "license_plate": "BRA-1023",
        "model": "Volvo FH16",
        "year": 2018,
        "description": "Caminhão de carga pesada com motor de alta potência"
    },
    {
        "license_plate": "KLM-4578",
        "model": "Mercedes-Benz Actros 2651",
        "year": 2020,
        "description": "Modelo versátil com foco em eficiência no transporte rodoviário"
    },
    {
        "license_plate": "XPZ-9931",
        "model": "Scania R 450",
        "year": 2019,
        "description": "Ideal para longas distâncias com excelente desempenho em economia"
    },
    {
        "license_plate": "GTR-2287",
        "model": "DAF XF 105",
        "year": 2016,
        "description": "Caminhão robusto com cabine confortável e bom custo-benefício"
    },
    {
        "license_plate": "HJK-7721",
        "model": "Iveco Stralis 480",
        "year": 2021,
        "description": "Alta tecnologia embarcada e baixo consumo de combustível"
    },
    {
        "license_plate": "LUV-3190",
        "model": "Volkswagen Constellation 24.280",
        "year": 2017,
        "description": "Bom desempenho urbano e rodoviário para médias cargas"
    },
    {
        "license_plate": "XYZ-9032",
        "model": "MAN TGX 28.440",
        "year": 2015,
        "description": "Modelo europeu confiável, ideal para transporte intermunicipal"
    },
    {
        "license_plate": "TYU-4556",
        "model": "Ford Cargo 2842",
        "year": 2014,
        "description": "Caminhão semipesado, econômico e de manutenção acessível"
    },
    {
        "license_plate": "ABC-6273",
        "model": "Mercedes-Benz Axor 2544",
        "year": 2022,
        "description": "Nova geração com foco em segurança e produtividade"
    },
    {
        "license_plate": "RPO-8855",
        "model": "Scania G 410",
        "year": 2013,
        "description": "Caminhão confiável com boa distribuição de torque e força"
    },
]


drivers = [
    {
        "name": "João da Silva",
        "birthday": date(1985, 7, 12),
        "cpf": "123.456.789-01",
        "driver_license": "MG1234567"
    },
    {
        "name": "Maria Aparecida Souza",
        "birthday": date(1979, 3, 28),
        "cpf": "987.654.321-00",
        "driver_license": "SP7654321"
    },
    {
        "name": "Carlos Eduardo Lima",
        "birthday": date(1990, 11, 2),
        "cpf": "345.678.901-22",
        "driver_license": "RJ2345678"
    },
    {
        "name": "Fernanda Oliveira Santos",
        "birthday": date(1987, 5, 19),
        "cpf": "567.890.123-44",
        "driver_license": "BA3456789"
    },
    {
        "name": "Paulo Henrique Machado",
        "birthday": date(1982, 8, 9),
        "cpf": "654.321.987-55",
        "driver_license": "RS4567890"
    },
    {
        "name": "Luciana Martins Pereira",
        "birthday": date(1995, 1, 22),
        "cpf": "321.654.987-66",
        "driver_license": "PR5678901"
    },
    {
        "name": "Ricardo Teixeira Rocha",
        "birthday": date(1980, 4, 30),
        "cpf": "111.222.333-44",
        "driver_license": "SC6789012"
    },
    {
        "name": "Adriana Costa Nunes",
        "birthday": date(1989, 9, 15),
        "cpf": "888.999.000-11",
        "driver_license": "CE7890123"
    },
    {
        "name": "Bruno Ferreira Ramos",
        "birthday": date(1992, 12, 6),
        "cpf": "444.555.666-77",
        "driver_license": "GO8901234"
    },
    {
        "name": "Elaine Cristina Barros",
        "birthday": date(1983, 6, 3),
        "cpf": "222.333.444-88",
        "driver_license": "PE9012345"
    },
]


trips = [
    {
        "start_city": "Goiânia-GO",
        "end_city": "Anápolis-GO",
        "start_date": datetime(2024, 6, 1, 7, 30, tzinfo=timezone.utc),
        "end_date": datetime(2024, 6, 1, 10, 0, tzinfo=timezone.utc),
        "description": "Entrega de medicamentos para centro hospitalar",
        "driver_id": 1,
        "truck_id": 1
    },
    {
        "start_city": "Trindade-GO",
        "end_city": "Aparecida de Goiânia-GO",
        "start_date": datetime(2024, 6, 2, 8, 15, tzinfo=timezone.utc),
        "end_date": datetime(2024, 6, 2, 11, 30, tzinfo=timezone.utc),
        "description": "Distribuição de produtos de limpeza",
        "driver_id": 2,
        "truck_id": 2
    },
    {
        "start_city": "Catalão-GO",
        "end_city": "Itumbiara-GO",
        "start_date": datetime(2024, 6, 3, 6, 45, tzinfo=timezone.utc),
        "end_date": datetime(2024, 6, 3, 14, 20, tzinfo=timezone.utc),
        "description": "Transporte de autopeças para concessionária",
        "driver_id": 3,
        "truck_id": 3
    },
    {
        "start_city": "Rio Verde-GO",
        "end_city": "Jataí-GO",
        "start_date": datetime(2024, 6, 4, 7, 0, tzinfo=timezone.utc),
        "end_date": datetime(2024, 6, 4, 12, 45, tzinfo=timezone.utc),
        "description": "Frete de grãos entre silos regionais",
        "driver_id": 4,
        "truck_id": 4
    },
    {
        "start_city": "Goiânia-GO",
        "end_city": "Formosa-GO",
        "start_date": datetime(2024, 6, 5, 5, 30, tzinfo=timezone.utc),
        "end_date": datetime(2024, 6, 5, 15, 0, tzinfo=timezone.utc),
        "description": "Transporte de móveis escolares",
        "driver_id": 5,
        "truck_id": 5
    },
    {
        "start_city": "Anápolis-GO",
        "end_city": "Luziânia-GO",
        "start_date": datetime(2024, 6, 6, 6, 0, tzinfo=timezone.utc),
        "end_date": datetime(2024, 6, 6, 13, 30, tzinfo=timezone.utc),
        "description": "Entrega de equipamentos agrícolas",
        "driver_id": 6,
        "truck_id": 6
    },
    {
        "start_city": "Trindade-GO",
        "end_city": "Goiânia-GO",
        "start_date": datetime(2024, 6, 7, 8, 0, tzinfo=timezone.utc),
        "end_date": datetime(2024, 6, 7, 9, 30, tzinfo=timezone.utc),
        "description": "Retorno com carga leve de papelaria",
        "driver_id": 7,
        "truck_id": 7
    },
    {
        "start_city": "Aparecida de Goiânia-GO",
        "end_city": "Catalão-GO",
        "start_date": datetime(2024, 6, 8, 7, 30, tzinfo=timezone.utc),
        "end_date": datetime(2024, 6, 8, 18, 15, tzinfo=timezone.utc),
        "description": "Transporte industrial entre filiais",
        "driver_id": 8,
        "truck_id": 8
    },
    {
        "start_city": "Itumbiara-GO",
        "end_city": "Formosa-GO",
        "start_date": datetime(2024, 6, 9, 6, 45, tzinfo=timezone.utc),
        "end_date": datetime(2024, 6, 9, 20, 0, tzinfo=timezone.utc),
        "description": "Carga refrigerada — laticínios e frios",
        "driver_id": 9,
        "truck_id": 9
    },
    {
        "start_city": "Luziânia-GO",
        "end_city": "Rio Verde-GO",
        "start_date": datetime(2024, 6, 10, 5, 15, tzinfo=timezone.utc),
        "end_date": datetime(2024, 6, 10, 21, 30, tzinfo=timezone.utc),
        "description": "Entrega de fertilizantes agrícolas",
        "driver_id": 10,
        "truck_id": 10
    }
]


maintenances = [
    {
        "truck_id": 1,
        "start_date": date(2024, 5, 10),
        "end_date": date(2024, 5, 12),
        "location": "Goiânia-GO",
        "description": "Troca de pneus e alinhamento"
    },
    {
        "truck_id": 2,
        "start_date": date(2024, 5, 15),
        "end_date": date(2024, 5, 17),
        "location": "Anápolis-GO",
        "description": "Revisão completa e troca de óleo"
    },
    {
        "truck_id": 3,
        "start_date": date(2024, 6, 1),
        "end_date": date(2024, 6, 2),
        "location": "Trindade-GO",
        "description": "Manutenção elétrica no sistema de faróis"
    },
    {
        "truck_id": 4,
        "start_date": date(2024, 6, 5),
        "end_date": date(2024, 6, 6),
        "location": "Aparecida de Goiânia-GO",
        "description": "Substituição de pastilhas de freio"
    },
    {
        "truck_id": 5,
        "start_date": date(2024, 6, 8),
        "end_date": date(2024, 6, 9),
        "location": "Catalão-GO",
        "description": "Reparo no sistema de ar-condicionado da cabine"
    },
]


indicators = {
    "fleet": {
        "total_trucks": 10,
        "trucks_in_maintenance": 5,
        "average_truck_year": 2017,
        "available_trucks": 5
    },
    "drivers": {
        "total_drivers": 10,
        "average_age": 39,
        "active_trips": 3
    },
    "trips": {
        "total_trips": 10,
        "trips_this_month": 10,
        "most_common_route": {
            "start_city": "Goiânia-GO",
            "end_city": "Anápolis-GO",
            "count": 2
        }
    },
    "maintenance": {
        "average_duration_days": 2.0,
        "locations_most_used": ["Goiânia-GO", "Anápolis-GO"]
    }
}
