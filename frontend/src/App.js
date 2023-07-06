import logo from "./logo.svg";
import "./App.css";
import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      empleadoList: [],
      modal: false,
      activeItem: {
        nombre: "",
        salario_base: "",
        horas_trabajadas: "",
        estado: false,
      },
    };
  }
  componentDidMount() {
    this.refreshList();
  }
  refreshList = () => {
    axios
      .get("/api/empleados/")
      .then((res) => this.setState({ empleadoList: res.data }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };
  handleSubmit = (item) => {
    this.toggle();

    if (item.id) {
      axios
        .put(`/api/empleados/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    axios.post("/api/empleados/", item).then((res) => this.refreshList());
  };
  handleDelete = (item) => {
    axios
      .delete(`/api/empleados/${item.id}/`)
      .then((res) => this.refreshList());
  };
  createItem = () => {
    const item = {
      nombre: "",
      salario_base: "",
      horas_trabajadas: "",
      estado: false,
    };
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  displayCompleted = (status) => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }
    return this.setState({ viewCompleted: false });
  };

  renderTabList = () => {
    return (
      <div className="nav nav-tabs">
        <span
          className={this.state.viewCompleted ? "nav-link active:" : "nav-link"}
          onClick={() => this.displayCompleted(true)}
        >
          Laborando
        </span>
        <span
          className={this.state.viewCompleted ? "nav-link" : "nav-link active"}
          onClick={() => this.displayCompleted(false)}
        >
          No Laborando
        </span>
      </div>
    );
  };
  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.empleadoList.filter(
      (item) => item.estado === viewCompleted
    );

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center bg-dark"
      >
        <span
          className={`empleado-nombre mr-2 text-light ${
            this.state.viewCompleted ? "completed-todo" : ""
          }`}
          title={item.nombre}
        >
          {item.nombre}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Editar
          </button>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDelete(item)}
          >
            Eliminar
          </button>
        </span>
      </li>
    ));
  };
  render() {
    return (
      <main className="container">
        <h1 className="text-primary bg-dark text-uppercase text-center my-4">
          Empleados Lista{" "}
        </h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="mb-4">
              <button className="btn btn-primary" onClick={this.createItem}>
                Agregar Empleado
              </button>
            </div>
            {this.renderTabList()}
            <ul className="list-group list-group-flush border-top-0">
              {this.renderItems()}
            </ul>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}
export default App;
