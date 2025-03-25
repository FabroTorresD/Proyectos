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


      async findByName(name: string): Promise<Trabajador | null> {
        try {
            const trabajador = await this.trabajadorRepository.findOne({ where: { name } });
            
            if (!trabajador) {
                console.log('No hay trabajadores con ese nombre');
                return null; // Explicitly return null if no trabajador is found
            }
    
            return trabajador; // Return the trabajador if found
        } catch (error) {
            console.error('Error al buscar trabajador:', error);
            throw new Error('Error al buscar trabajador'); // Throw the error to handle it properly elsewhere
        }
    }
    
}

