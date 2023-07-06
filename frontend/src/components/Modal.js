import React, { Component } from "react";

import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;
    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }
    const activeItem = { ...this.state.activeItem, [name]: value };
    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Editar datos del empleado</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="empleado-nombre">Nombre</Label>
              <Input
                type="text"
                id="empleado-nombre"
                name="nombre"
                value={this.state.activeItem.nombre}
                onChange={this.handleChange}
                placeholder="Ingrese nombre del empleado"
              />
            </FormGroup>
            <FormGroup>
              <Label for="empleado-salario_base">Salario Base</Label>
              <Input
                type="text"
                id="empleado-salario_base"
                name="salario_base"
                value={this.state.activeItem.salario_base}
                onChange={this.handleChange}
                placeholder="Ingrese el salario del Empleado "
              />
            </FormGroup>
            <FormGroup>
              <Label for="empleado-horas_trabajadas">Horas trabajadas</Label>
              <Input
                type="text"
                id="empleado-horas_trabajadas"
                name="horas_trabajadas"
                value={this.state.activeItem.horas_trabajadas}
                onChange={this.handleChange}
                placeholder="Ingrese horas trabajadas del empleado"
              />
            </FormGroup>
            <FormGroup check>
              <Label check>
                <Input
                  type="checkbox"
                  name="estado"
                  checked={this.state.activeItem.estado}
                  onChange={this.handleChange}
                />
                Laborando
              </Label>
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button color="success" onClick={() => onSave(this.state.activeItem)}>
            Guardar
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}
