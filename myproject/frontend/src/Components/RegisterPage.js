import { useState } from "react";
import { Form, Button, Col } from "react-bootstrap";
import { Container, Row } from "react-bootstrap";

const RegisterPage = () => {
  const [login, setLogin] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [surname, setSurname] = useState("");
  const [email, setEmail] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");

  const handleRegister = () => {
    window.localStorage.setItem("/app/login", login);
    window.localStorage.setItem("/app/password", password);
  };

  return (
    <Form className="center">
      <Container>
        <Row>
          <Col>
            <Form.Group controlId="formLogin">
              <Form.Label>Login</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter your login"
                onChange={({ target }) => setLogin(target.value)}
              />
            </Form.Group>
          </Col>
        </Row>
        <Row>
          <Col>
            <Form.Group controlId="formPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter your password"
                onChange={({ target }) => setPassword(target.value)}
              />
            </Form.Group>
          </Col>
        </Row>
        <Row>
          <Col>
            <Button
              variant="primary"
              type="submit"
              onClick={() => handleRegister()}
            >
              Submit
            </Button>
          </Col>
        </Row>
      </Container>
    </Form>
  );
};

export default RegisterPage;
