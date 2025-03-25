import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Area } from 'src/entities/area.entity';
import { Repository } from 'typeorm';
import { areaDto } from './dto/area.dto';
import { error } from 'console';

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
    
    async create(areaDto : areaDto) : Promise<Area>{
        const existingArea = await this.areaRepository.findOne({where : {name: areaDto.name}})
        
        if (existingArea){
            throw new error('NOMBRE DE AREA EXISTENTE')
        }
        
        const area = this.areaRepository.create(areaDto)
        return await this.areaRepository.save(area)
    }


}