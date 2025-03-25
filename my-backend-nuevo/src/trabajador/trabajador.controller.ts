import { Controller, Get } from '@nestjs/common';
import { TrabajadorService } from './trabajador.service'; 
import { Trabajador } from 'src/entities/trabajador.entity';

@Controller('/api/trabajadores')
export class TrabajadorController {
  constructor(private readonly trabajadorService: TrabajadorService) {}

  @Get()
  async findAll(): Promise<Trabajador[]> {
    return this.trabajadorService.findAll(); // Llama al servicio que obtiene todos los trabajadores
  }
}
