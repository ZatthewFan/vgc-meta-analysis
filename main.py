from fetch_and_parse import FetchFromURL
from database import execute_script

setup_script = ''' CREATE TABLE IF NOT EXISTS pokemon (
                        pkm_id      int PRIMARY KEY,
                        name        varchar(40) NOT NULL,
                        item        varchar(30),
                        ability     varchar(20) NOT NULL,
                        level       int,
                        tera        varchar(10),
                        nature      varchar(10)
                    );
                    
                    CREATE TABLE IF NOT EXISTS ev (
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
                    
                    CREATE TABLE IF NOT EXISTS iv (
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
                    
                    CREATE TABLE IF NOT EXISTS moveset (
                        moveset_id  int PRIMARY KEY,
                        slot1       varchar(30) NOT NULL,
                        slot2       varchar(30),
                        slot3       varchar(30),
                        slot4       varchar(30),
                        pkm_id      int NOT NULL,
                        FOREIGN KEY (pkm_id) REFERENCES pokemon(pkm_id)
                    );
                    
                    CREATE TABLE IF NOT EXISTS type (
                        type_id     int PRIMARY KEY,
                        type1       varchar(20) NOT NULL,
                        type2       varchar(20),
                        pkm_id      int NOT NULL,
                        FOREIGN KEY (pkm_id) REFERENCES pokemon(pkm_id)
                    );
                    
                    CREATE TABLE IF NOT EXISTS  base_stats (
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
                    
                    CREATE TABLE IF NOT EXISTS  total_stats (
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
                    
                    CREATE TABLE IF NOT EXISTS  weaknesses (
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
                    
                    CREATE TABLE IF NOT EXISTS  team (
                        team_id     int PRIMARY KEY,
                        format      varchar(30) NOT NULL,
                        is_ots      boolean NOT NULL
                    );
                    
                    CREATE TABLE IF NOT EXISTS teamlist (
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

if __name__ == "__main__":
    url_fetcher = FetchFromURL("https://victoryroadvgc.com/sv-rental-teams/", "gen9vgc2023regulationg")
    teams = url_fetcher.fetch()
    print("fetched!")

    execute_script(setup_script)
    print("finished setting up database")
