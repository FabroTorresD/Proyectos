import { Controller, Get, Param } from '@nestjs/common';
import { AreaService } from './area.service';
import { Area } from 'src/entities/area.entity';


@Controller('/api/area')
export class AreaController {
    constructor(private readonly areaService: AreaService ){}

    @Get()
    async findAll(): Promise<Area[]> {
        return this.areaService.findAll(); 
    }
    
    @Get(':id')
    async findById(@Param('id') id: number): Promise <Area | null> {
        return this.areaService.findById(id);
    }
}
