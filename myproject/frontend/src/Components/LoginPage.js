import axios from "axios";
import { useState } from "react";
import { Form, Button, Col } from "react-bootstrap";
import { Container, Row } from "react-bootstrap";
import { Link } from "react-router-dom";
import "./css/index.css";

const LoginPage = () => {
  const [login, setLogin] = useState("");
  const [password, setPassword] = useState("");
  const [isLoginInvalid, setIsLoginInvalid] = useState(false);
  const [isPasswordInvalid, setIsPasswordInvalid] = useState(false);
  const [isFormValid, setIsFormValid] = useState();

  const handleLogin = () => {
    if (login !== "" && password !== "") {
      axios
        .post(`http://localhost:8000/app/login/`, {
          login: login,
          password: password,
        })
        .then((res) => {
          let content = JSON.parse(res.data);
          console.log(content[0].fields);
          const { login, password, user } = content[0].fields;
          localStorage.setItem("login", login);
          localStorage.setItem("password", password);
          localStorage.setItem("user_id", user);
          setIsFormValid(true);
          setIsPasswordInvalid(false);
          setIsLoginInvalid(false);
        })
        .catch((e) => {
          const { error } = e.response.data;
          if (error == "Invalid login") {
            setIsLoginInvalid(true);
          } else if (error == "Invalid password") {
            setIsPasswordInvalid(true);
          }
          console.log("Login: " + login);
          console.log("Password: " + password);
          setIsFormValid(false);
        });
    } else {
      if (login === "") {
        setIsLoginInvalid(true);
      }
      if (password === "") {
        setIsPasswordInvalid(true);
      }
    }
  };

  return (
    <Form className="center">
      <Container>
        <Row>
          <Col>
            <Form.Group controlId="formLogin">
              <Form.Label>Login</Form.Label>
              <Form.Control
                isInvalid={isLoginInvalid}
                isValid={isFormValid ? true : undefined}
                type="text"
                placeholder="Enter your login"
                onChange={({ target }) => setLogin(target.value)}
              />
              <Form.Control.Feedback>Login is valid.</Form.Control.Feedback>
              <Form.Control.Feedback type="invalid">
                Please provide a valid login.
              </Form.Control.Feedback>
            </Form.Group>
          </Col>
        </Row>
        <Row>
          <Col>
            <Form.Group controlId="formPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                isInvalid={isPasswordInvalid}
                isValid={isFormValid ? true : undefined}
                type="password"
                placeholder="Enter your password"
                onChange={({ target }) => setPassword(target.value)}
              />
              <Form.Control.Feedback>Password is valid.</Form.Control.Feedback>
              <Form.Control.Feedback type="invalid">
                Please provide a valid password.
              </Form.Control.Feedback>
            </Form.Group>
          </Col>
        </Row>
        <Row>
          <Col>
            <Button
              variant="primary"
              type="submit"
              onClick={(e) => {
                e.preventDefault();
                handleLogin();
              }}
            >
              Submit
            </Button>
          </Col>
          <Col>
            <Button variant="secondary">
              <Link style={{ color: "white" }} to={"/register"}>
                Register
              </Link>
            </Button>
          </Col>
        </Row>
      </Container>
    </Form>
  );
};

export default LoginPage;
