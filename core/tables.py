category = """
           CREATE TABLE IF NOT EXISTS category
           (
               id      BIGSERIAL PRIMARY KEY,
               user_id BIGINT REFERENCES users (id) ON DELETE CASCADE,
               title   VARCHAR(255) NOT NULL UNIQUE
           ) \
           """

books = """
        CREATE TABLE IF NOT EXISTS books
        (
            id          BIGSERIAL PRIMARY KEY,
            user_id     BIGINT REFERENCES users (id) ON DELETE CASCADE,
            category_id BIGINT       REFERENCES category (id) ON DELETE SET NULL,
            name        VARCHAR(255) NOT NULL UNIQUE,
            author      VARCHAR(255),
            note        TEXT,
            status      VARCHAR(32)  NOT NULL,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) \
        """


users = """
        CREATE TABLE IF NOT EXISTS users
        (
            id         BIGSERIAL PRIMARY KEY,
            email      VARCHAR(255) NOT NULL UNIQUE,
            password   VARCHAR(255),
            is_login   BOOLEAN DEFAULT FALSE,
            is_active  BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) \
        """

codes = """
        CREATE TABLE IF NOT EXISTS codes
        (
            id         BIGSERIAL PRIMARY KEY,
            email      VARCHAR(255) NOT NULL UNIQUE,
            code       VARCHAR(6),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) \
        """