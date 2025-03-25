import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Trabajador } from 'src/entities/trabajador.entity';

@Injectable()
export class TrabajadorService {
    constructor(
        @InjectRepository(Trabajador)
        private trabajadorRepository: Repository<Trabajador>
    ) {}

    async findAll(): Promise<Trabajador[]> {
        return this.trabajadorRepository.find(); // Usa el repositorio para obtener los datos
      }
}

