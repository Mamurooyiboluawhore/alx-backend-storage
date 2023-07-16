-- 5-valid_email.sql

DELIMITER $$
CREATE TRIGGER resetEmail
AFTER UPDATE ON users
FOR EACH ROW 
BEGIN
        IF OLD.email != NEW.email THEN
            SET valid_email = 0;
        END IF;
END;
$$
DELIMITER ;
