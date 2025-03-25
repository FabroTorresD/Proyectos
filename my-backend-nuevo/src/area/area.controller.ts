import { Controller, Get, Param, Post , Body, Put} from '@nestjs/common';
import { AreaService } from './area.service';
import { Area } from 'src/entities/area.entity';
import { areaDto } from './dto/area.dto';


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


    @Post()
    async create(@Body() areaDto :areaDto): Promise<Area>{
    
        return this.areaService.create(areaDto);
    }


    @Put()
  async update(@Body() areaDto: areaDto) {
    return this.areaService.updateArea(areaDto);
  }
    }
