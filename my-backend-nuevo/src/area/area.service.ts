import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Area } from 'src/entities/area.entity';
import { Repository } from 'typeorm';

@Injectable()
export class AreaService {
    constructor(
        @InjectRepository(Area) 
        private areaRepository: Repository<Area>   
    ){}

    async findAll(): Promise<Area[] > {
        return this.areaRepository.find();
    }

    async findById(id: number): Promise<Area | null> {
        return this.areaRepository.findOne({
            where: { id }, 
        });
    }
    
}