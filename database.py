import psycopg2
from dotenv import find_dotenv, load_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASS = os.getenv("POSTGRES_PASS")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

conn = None
cur = None

try:
    conn = psycopg2.connect(
        database = POSTGRES_DB,
        host = POSTGRES_HOST,
        user = POSTGRES_USER,
        password = POSTGRES_PASS,
        port = POSTGRES_PORT
        )
    
    cur = conn.cursor()
    
    create_script = ''' CREATE TABLE IF NOT EXISTS pokemon (
                            pkm_id      int PRIMARY KEY,
                            name        varchar(40) NOT NULL,
                            item        varchar(30),
                            ability     varchar(20) NOT NULL,
                            level       int,
                            tera        varchar(10),
                            nature      varchar(10)
                        );
                        
                        CREATE TABLE IF NOT EXITS ev (
                            ev_id       int PRIMARY KEY,
                            hp          int NOT NULL,
                            atk         int NOT NULL,
                            def         int NOT NULL,
                            spa         int NOT NULL,
                            spd         int NOT NULL,
                            spe         int NOT NULL,
                            pkm_id      int NOT NULL,
                            FOREIGN KEY (pkm_id) REFERENCES pokemon(pkm_id)
                        );
                        
                        CREATE TABLE IF NOT EXITS iv (
                            iv_id       int PRIMARY KEY,
                            hp          int NOT NULL,
                            atk         int NOT NULL,
                            def         int NOT NULL,
                            spa         int NOT NULL,
                            spd         int NOT NULL,
                            spe         int NOT NULL,
                            pkm_id      int NOT NULL,
                            FOREIGN KEY (pkm_id) REFERENCES pokemon(pkm_id)
                        );
                        
                        CREATE TABLE IF NOT EXITS moveset (
                            moveset_id  int PRIMARY KEY,
                            slot1       varchar(30) NOT NULL,
                            slot2       varchar(30),
                            slot3       varchar(30),
                            slot4       varchar(30),
                            pkm_id      int NOT NULL,
                            FOREIGN KEY (pkm_id) REFERENCES pokemon(pkm_id)
                        );
                        
                        CREATE TABLE IF NOT EXITS type (
                            type_id     int PRIMARY KEY,
                            type1       varchar(20) NOT NULL,
                            type2       varchar(20),
                            pkm_id      int NOT NULL,
                            FOREIGN KEY (pkm_id) REFERENCES pokemon(pkm_id)
                        );
                        
                        CREATE TABLE IF NOT EXITS  base_stats (
                            bstat_id    int PRIMARY KEY,
                            hp          int NOT NULL,
                            atk         int NOT NULL,
                            def         int NOT NULL,
                            spa         int NOT NULL,
                            spd         int NOT NULL,
                            spe         int NOT NULL,
                            pkm_id      int NOT NULL,
                            FOREIGN KEY (pkm_id) REFERENCES pokemon(pkm_id)
                        );
                        
                        CREATE TABLE IF NOT EXITS  total_stats (
                            tstat_id    int PRIMARY KEY,
                            hp          int NOT NULL,
                            atk         int NOT NULL,
                            def         int NOT NULL,
                            spa         int NOT NULL,
                            spd         int NOT NULL,
                            spe         int NOT NULL,
                            pkm_id      int NOT NULL,
                            FOREIGN KEY (pkm_id) REFERENCES pokemon(pkm_id)
                        );
                        
                        CREATE TABLE IF NOT EXITS  weaknesses (
                            weakness_id int PRIMARY KEY,
                            normal      float NOT NULL,
                            fire        float NOT NULL,
                            water       float NOT NULL,
                            electric    float NOT NULL,
                            grass       float NOT NULL,
                            ice         float NOT NULL,
                            fighting    float NOT NULL,
                            poison      float NOT NULL,
                            ground      float NOT NULL,
                            flying      float NOT NULL,
                            psychic     float NOT NULL,
                            bug         float NOT NULL,
                            rock        float NOT NULL,
                            ghost       float NOT NULL,
                            dragon      float NOT NULL,
                            dark        float NOT NULL,
                            steel       float NOT NULL,
                            fairy       float NOT NULL,
                            pkm_id      int NOT NULL,
                            FOREIGN KEY (pkm_id) REFERENCES pokemon(pkm_id)
                        );
                        
                        CREATE TABLE IF NOT EXITS  team (
                            team_id     int PRIMARY KEY,
                            format      varchar(30) NOT NULL,
                            is_ots      boolean NOT NULL
                        );
                        
                        CREATE TABLE IF NOT EXITS teamlist (
                            teamlist_id int PRIMARY KEY,
                            pkm1_id     int NOT NULL,
                            pkm2_id     int NOT NULL,
                            pkm3_id     int NOT NULL,
                            pkm4_id     int NOT NULL,
                            pkm5_id     int NOT NULL,
                            pkm6_id     int NOT NULL,
                            team_id     int NOT NULL,
                            FOREIGN KEY (pkm1_id) REFERENCES pokemon(pkm_id),
                            FOREIGN KEY (pkm2_id) REFERENCES pokemon(pkm_id),
                            FOREIGN KEY (pkm3_id) REFERENCES pokemon(pkm_id),
                            FOREIGN KEY (pkm4_id) REFERENCES pokemon(pkm_id),
                            FOREIGN KEY (pkm5_id) REFERENCES pokemon(pkm_id),
                            FOREIGN KEY (pkm6_id) REFERENCES pokemon(pkm_id),
                            FOREIGN KEY (team_id) REFERENCES team(team_id)
                        );
                        '''
    
    cur.execute(create_script)
    conn.commit()
    
except Exception as error:
    print(error)
finally:
    if cur is not None: cur.close()
    if conn is not None: conn.close()
