
import logo from './logo.svg';
import './App.css';


function App() {
  return (
    <div className="container py-4">
      {/* Navegación Bootstrap */}
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <a className="navbar-brand" href="#">OctoFit Tracker</a>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item active">
              <a className="nav-link" href="#">Inicio</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Perfil</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Equipos</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Leaderboard</a>
            </li>
          </ul>
        </div>
      </nav>

      {/* Encabezado */}
      <h1 className="display-4 mb-4 text-center">Bienvenido a OctoFit Tracker</h1>

      {/* Tarjeta Bootstrap */}
      <div className="card mb-4 mx-auto" style={{maxWidth: '28rem'}}>
        <div className="card-body text-center">
          <img src={logo} className="App-logo mb-3" alt="logo" style={{width: '100px'}} />
          <h5 className="card-title">¡Comienza a registrar tus actividades!</h5>
          <p className="card-text">Edita <code>src/App.js</code> y guarda para recargar.</p>
          <a href="https://reactjs.org" className="btn btn-primary" target="_blank" rel="noopener noreferrer">
            Aprende React
          </a>
        </div>
      </div>

      {/* Tabla Bootstrap de ejemplo */}
      <h2 className="h4 mb-3">Tus actividades recientes</h2>
      <table className="table table-striped table-bordered">
        <thead className="table-primary">
          <tr>
            <th>Fecha</th>
            <th>Actividad</th>
            <th>Duración</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>2026-04-17</td>
            <td>Correr</td>
            <td>30 min</td>
            <td><button className="btn btn-sm btn-outline-info">Ver</button></td>
          </tr>
          <tr>
            <td>2026-04-16</td>
            <td>Bicicleta</td>
            <td>45 min</td>
            <td><button className="btn btn-sm btn-outline-info">Ver</button></td>
          </tr>
        </tbody>
      </table>

      {/* Formulario Bootstrap de ejemplo */}
      <h2 className="h4 mb-3">Registrar nueva actividad</h2>
      <form className="mb-5">
        <div className="mb-3">
          <label htmlFor="actividad" className="form-label">Actividad</label>
          <input type="text" className="form-control" id="actividad" placeholder="Ej: Correr" />
        </div>
        <div className="mb-3">
          <label htmlFor="duracion" className="form-label">Duración (minutos)</label>
          <input type="number" className="form-control" id="duracion" placeholder="Ej: 30" />
        </div>
        <button type="submit" className="btn btn-success">Registrar</button>
      </form>

      {/* Modal Bootstrap de ejemplo (estructura, requiere JS para funcionar) */}
      <div className="modal fade" id="exampleModal" tabIndex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="exampleModalLabel">Modal de ejemplo</h5>
              <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div className="modal-body">
              Aquí puedes mostrar información adicional o formularios.
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
              <button type="button" className="btn btn-primary">Guardar cambios</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
